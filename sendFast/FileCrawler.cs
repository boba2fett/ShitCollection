using System;
using System.IO;
using System.Text.RegularExpressions;

namespace send
{
    class FileCrawler
    {
        protected void myHandler(object sender, ConsoleCancelEventArgs args)
        {
            args.Cancel = true;
            Cancel();
        }
        public void Cancel()
        {
            _canceled=true;
        }
        bool _canceled=false;
        bool _found=false;
        DbWriter _dbw=new DbWriter();
        public void Start()
        {
            Console.CancelKeyPress += new ConsoleCancelEventHandler(myHandler);
            var dc=_dbw.Latest();
            var timeStart=DateTime.Now;
            int idStart=-1;
            if(dc==null)
            {
                Console.WriteLine($"Last Id = {idStart}");
                Console.WriteLine($"Time = {timeStart}");
                Crawl();
            }
            else
            {
                idStart=dc.Id;
                Console.WriteLine($"Last Id = {idStart}");
                Console.WriteLine($"Time = {timeStart}");
                Console.WriteLine($"{dc.User}@{dc.Domain}:{dc.Password}");
                Crawl(dc);
            }
            _dbw.Save();
            dc=_dbw.Latest();
            var timeEnd=DateTime.Now;
            var idEnd=dc.Id;
            Console.WriteLine($"Last Id = {idEnd}");
            Console.WriteLine($"Time = {timeEnd}");
            var t=timeEnd-timeStart;
            var ids=idEnd-idStart;
            Console.WriteLine($"Total Time = {t}");
            Console.WriteLine($"Total Ids = {ids}");
            double ratio=((double)ids)/((double)t.TotalSeconds);
            Console.WriteLine($"Ratio per Sec = {ratio}");
        }
        public void Crawl()
        {
            foreach(var file in Directory.GetFiles(Config.Data,"*", SearchOption.AllDirectories)) if (!_canceled)
            {
                Process(file);
            }
        }

        public void Crawl(DataColl dc)
        {
            try{
                foreach(var file in Directory.GetFiles(Config.Data,"*", SearchOption.AllDirectories)) if (!_canceled)
                {
                    if(!_found)
                    {
                        //Console.WriteLine($"Searching in {file}\r");
                        var filename=file;
                        if(!filename.Contains("symbols"))
                        {
                            filename=filename.Remove(0,Config.Data.Length);
                            filename=filename.Replace("/",string.Empty);
                            if(dc.User.ToLower().StartsWith(filename))
                            {
                                Console.WriteLine(file);
                                Process(file,dc);
                            }
                        }
                        else
                        {
                            filename=filename.Replace("symbols","[^a-z0-9]");
                            filename=filename.Remove(0,Config.Data.Length);
                            filename=filename.Replace("/",string.Empty);
                            Regex rgx = new Regex("^"+filename, RegexOptions.IgnoreCase);
                            MatchCollection matches = rgx.Matches(dc.User);
                            if (matches.Count > 0)
                            {
                                Console.WriteLine(file);
                                Process(file,dc);
                            }
                        }
                    }
                    else
                    {
                        Process(file);
                    }
                }
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error Crawling: {e}");
            }
        }

        public void Process(string filePath)
        {
            using(System.IO.StreamReader file = new System.IO.StreamReader(filePath))
            {
                int count=0;
                string line;
                while((line = file.ReadLine()) != null&&!_canceled)  
                {
                    if(count==1000)
                    {
                        _dbw.Save();
                        count=0;
                    }
                    ProcessLine(line);
                    count++;
                }
                file.Close();
                _dbw.Save();
            }
            if(!_canceled)
            {
                Console.WriteLine($"Processed File: {filePath}");
            }
        }

        public void Process(string filePath, DataColl dc)
        {
            using(System.IO.StreamReader file = new System.IO.StreamReader(filePath))
            {
                int count=0;
                string line;
                while((line = file.ReadLine()) != null && !_canceled)
                {
                    if(_found)
                    {
                        if(count==1000)
                        {
                            _dbw.Save();
                            count=0;
                        }
                        ProcessLine(line);
                        count++;
                    }
                    if(line.StartsWith(dc.User)&&line.EndsWith(dc.Password))
                    {
                        Console.WriteLine("Found");
                        _found=true;
                    }
                }
                file.Close();
                _dbw.Save();
            }
            if(!_canceled)
            {
                Console.WriteLine($"Processed File: {filePath}");
            }
        }

        public void ProcessLine(string line)
        {
            int emailSeperator=line.IndexOf("@");
            if(emailSeperator==-1)
            {
                ProblemForLater(line);
                return;
            }
            int pwdSeperator=-1;
            foreach(var seperator in Config.Seperators) if (pwdSeperator==-1)
            {
                pwdSeperator=line.IndexOf(seperator);
            }
            int domainLegth=pwdSeperator-emailSeperator-1;
            if(domainLegth<0)
            {
                ProblemForLater(line);
                return;
            }
            string pwd=null;
            string domain=line.Substring(emailSeperator+1);
            if(pwdSeperator!=-1)
            {
                pwd=line.Substring(pwdSeperator+1);
                domain=line.Substring(emailSeperator+1,domainLegth);
            }
            string user=line.Substring(0,emailSeperator);
            
            if(!_dbw.Insert(user,domain,pwd))
            {
                Console.WriteLine("Fail At Db stopping");
                Cancel();
            }
        }

        public void ProblemForLater(string line)
        {
            string path = Config.ProblemForLater;
            using (StreamWriter sw = File.AppendText(path))
            {
                sw.WriteLine(line);
            }
        }
    }
}
