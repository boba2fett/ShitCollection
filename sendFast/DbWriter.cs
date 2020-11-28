using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using System.Linq;

namespace send
{
    public class DataContext : DbContext
    {
        public DbSet<DataColl> Data { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder options)
            => options.UseSqlite($@"Data Source={Config.Db}");
    }

    public class DataColl
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        [Key, Column(Order = 0)]
        public int Id { get; set; }
        public string User { get; set; }
        public string Domain { get; set; }
        public string Password { get; set; }
    }

    class DbWriter
    {
        private DataContext _dc=new DataContext();
        public DbWriter()
        {
            try{
                _dc.Database.Migrate();
            }
            catch(Exception ex)
            {
                Console.WriteLine($"Probably hramless, because Database is already created: {ex}");
            }
        }

        public bool Insert(string user,string domain, string pwd)
        {
            try
            {
                _dc.Add(new DataColl{ User=user,Domain=domain,Password=pwd });
                
                return true;
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error Writing: {e}");
                return false;
            }
        }

        public bool Save()
        {
            try{
                _dc.SaveChanges();
                return true;
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error getting Last: {e}");
            }
            return false;
        }

        public DataColl Latest()
        {
            try{
                var result = _dc.Data.OrderByDescending(b => b.Id);
                if(result.Any())
                {
                    Console.WriteLine("Database Queryable");
                    return result.First();
                }
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error getting Last: {e}");
            }
            return null;
        }
    }
}
