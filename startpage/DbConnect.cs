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
        public DbSet<User> User { get; set; }
        public DbSet<Profiles> Profiles { get; set; }
        public DbSet<Sites> Sites { get; set; }
        public DbSet<ProfilesSites> ProfilesSites { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder options)
            => options.UseSqlite(@"Data Source=database.db");
    }

    public class User
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        [Key, Column(Order = 0)]
        public int Id { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
    }

    class DbWriter
    {
        public DbWriter()
        {
            try{
                using(DataContext dc=new DataContext())
                {
                    dc.Database.Migrate();
                }
            }
            catch(Exception ex)
            {
                Console.WriteLine($"Probably hramless, because Database is already created: {ex}");
            }
        }
        public bool Insert(string email, string pwd)
        {
            try
            {
                using(DataContext dc=new DataContext())
                {
                    dc.Add(new DataColl{ Email=email,Password=pwd });
                    dc.SaveChanges();
                    return true;
                }
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error Writing: {e}");
                return false;
            }
        }

        public DataColl Latest()
        {
            using(DataContext dc=new DataContext())
            {
                var result = dc.Data.OrderByDescending(b => b.Id);
                if(result.Any())
                {
                    Console.WriteLine("Database Queryable");
                    return result.First();
                }
            }
            return null;
        }
    }
}
