using System.Collections.Generic;

namespace send
{
    class Program
    {
        
        static void Main(string[] args)
        {
            FileCrawler fc=new FileCrawler();
            fc.Start();
        }
    }
    static class Config
    {
        public static string PrePath { get{return "/home/bf/git/ShitCollection/sendFast/";}}
        public static string Data {get{return PrePath+"data/";}}
        public static string Db {get{return PrePath+"db/pwdata.db";}}
        public static string ProblemForLater {get{return "db/problemForLater";}}
        public static List<string> Seperators {
            get{
                return new List<string>{
                    ":",
                    ";",
                    "\t",
                    "|"
                };
            }
        }

    }
}
