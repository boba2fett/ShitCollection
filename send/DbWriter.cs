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
            => options.UseSqlite(@"Data Source=/media/bf/Elements SE/REALdata/tr/pwdata.db");
    }

    public class DataColl
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        [Key, Column(Order = 0)]
        public int Id { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
    }

    class DbWriter
    {

        public void Insert(string email, string pwd)
        {
            try{
                using (var dc = new DataContext())
                {
                    dc.Add(new DataColl{ Email=email,Password=pwd });
                    dc.SaveChanges();
                }
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error Sending: {e}");
            }
        }

        public DataColl Latest()
        {
            DataColl result=null;
            using (var dc = new DataContext())
            {
                result=dc.Data.OrderByDescending(b => b.Id).First();
            }
            return result;
        }
    }
}
