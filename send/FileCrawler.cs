using System;
using System.IO;

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
        SendData _sd=new SendData();
        public void Start()
        {
            Console.CancelKeyPress += new ConsoleCancelEventHandler(myHandler);
            var dc=_dbw.Latest();
            var timeStart=DateTime.Now;
            var idStart=dc.Id;
            if(dc==null)
            {
                Crawl();
            }
            else
            {
                Console.WriteLine($"Last Id= {idStart}");
                Console.WriteLine($"Time= {timeStart}");
                Crawl(dc);
            }
            dc=_dbw.Latest();
            var timeEnd=DateTime.Now;
            var idEnd=dc.Id;
            Console.WriteLine($"Last Id= {idEnd}");
            Console.WriteLine($"Time= {timeEnd}");
            var t=timeEnd-timeStart;
            var ids=idEnd-idStart;
            Console.WriteLine($"Total Time= {t}");
            Console.WriteLine($"Total Ids= {ids}");
            double ratio=((double)ids)/((double)t.Seconds);
            Console.WriteLine($"Ratio per Sec= {ratio}");
        }
        public void Crawl()
        {
            foreach(var file in Directory.GetFiles(@"/media/bf/Elements SE/REALdata/tr/BreachCompilation/data/","*", SearchOption.AllDirectories))
            {
                if(!_canceled)
                {
                    Process(file);
                }
                else
                {
                    return;
                }
            }
        }

        public void Crawl(DataColl dc)
        {
            try{
                foreach(var file in Directory.GetFiles(@"/media/bf/Elements SE/REALdata/tr/BreachCompilation/data/","*", SearchOption.AllDirectories))
                {
                    if(!_found)
                    {
                        var filename=file;
                        filename=filename.Remove(0,@"/media/bf/Elements SE/REALdata/tr/BreachCompilation/data/".Length);
                        filename=filename.Replace("/",string.Empty);
                        if(dc.Email.StartsWith(filename))
                        {
                            Console.WriteLine(file);
                            if(!_canceled)
                            {
                                Process(file,dc);
                            }
                            else
                            {
                                return;
                            }
                        }
                    }
                    else
                    {
                        if(!_canceled)
                        {
                            Process(file);
                        }
                        else
                        {
                            return;
                        }
                    }
                }
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error Crwling: {e}");
            }
        }

        public void Process(string filePath)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(filePath);
            string line;
            while((line = file.ReadLine()) != null)  
            {
                if(!_canceled)
                {
                    ProcessLine(line);
                }
                else
                {
                    return;
                }
            }
        }

        public void Process(string filePath, DataColl dc)
        {
            System.IO.StreamReader file = new System.IO.StreamReader(filePath);
            string line;
            while((line = file.ReadLine()) != null)  
            {
                if(_found)
                {
                    if(!_canceled)
                    {
                        ProcessLine(line);
                    }
                    else
                    {
                        return;
                    }
                }
                if(line.StartsWith(dc.Email)&&line.EndsWith(dc.Password))
                {
                    Console.WriteLine("Found");
                    _found=true;
                }
            }
        }

        public void ProcessLine(string line)
        {
            int indx=line.IndexOf(":");
            if(indx==-1)
            {
                indx=line.IndexOf(";");
                if(indx==-1)
                {
                    indx=line.IndexOf("\t");
                }
            }
            if(indx==-1)
            {
                ProblemForLater(line);
                return;
            }
            string email=line.Substring(0,indx);
            string pwd=line.Substring(indx+1);
            _dbw.Insert(email,pwd);
            _sd.Send(email,pwd);
        }

        public void ProblemForLater(string line)
        {
            string path = @"/media/bf/Elements SE/REALdata/tr/problemForlater";
            if (!File.Exists(path))
            {
                using (StreamWriter sw = File.CreateText(path))
                {

                }	
            }

            using (StreamWriter sw = File.AppendText(path))
            {
                sw.WriteLine(line);
            }
        }
    }
}
