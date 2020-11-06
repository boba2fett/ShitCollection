using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.ChangeTracking;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Configuration;

namespace TraceDiagramm
{
    public interface IDCDataContext
    {
        public DatabaseFacade Database { get; }
        DbSet<DCData> DcOn { get; set; }
        int SaveChanges();
        EntityEntry Add(object entity);
    }

    public class DCDataContext : DbContext, IDCDataContext
    {
        public DbSet<DCData> DcOn { get; set; }
        private readonly IConfiguration _configuration;
        public DCDataContext(DbContextOptions<DCDataContext> options, IConfiguration configuration) : base(options)
        {
            _configuration = configuration;
        }

        public DCDataContext(IConfiguration configuration)
        {
            _configuration = configuration;
        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                var prepath=_configuration.GetValue<string>("prepath");
                optionsBuilder.UseSqlite($"Data Source={prepath}/etc/python-shit/dcdata.db");
            }

        }


    }

    public interface IDbConnect
    {
        DiagramData GetDiaData(int cap);
        void ensureCreated();
    }

    public class DbConnect : IDbConnect
    {
        private readonly ILogger _logger;
        private readonly IDCDataContext _bdContext;
        private readonly IConfiguration _configuration;
        public DbConnect(IDCDataContext bdContext, ILogger<DbConnect> logger, IConfiguration configuration)
        {
            _configuration = configuration;
            _bdContext = bdContext;
            _logger = logger;
        }

        public DbConnect(ILogger<DbConnect> logger, IConfiguration configuration)
        {
            _configuration = configuration;
            // var options = new DbContextOptionsBuilder<DCDataContext>()
            //     .UseSqlServer(configuration.GetConnectionString("database1"))
            //     .Options;
            _bdContext = new DCDataContext(configuration);
            _logger = logger;
        }

        public DiagramData GetDiaData(int cap)
        {
            
            _logger.LogInformation("Diagram Data is selected from Database");
            var diaData = new DiagramData();
            diaData.Categories = new List<DCCategory>();
            var names=_bdContext.DcOn.Select(d=>d.User).Distinct();
            foreach (var name in names)
            {
                var selectedList = _bdContext.DcOn.Where(b => b.User == name).OrderByDescending(b => b.Timestamp).Take(cap).ToList();
                
                var category = new DCCategory()
                {
                    Label = name,
                    Data = new List<DCPair>()
                };

                foreach (var selected in selectedList)
                {
                    category.Data.Add(new DCPair
                        {
                        X = selected.Timestamp,
                        Y = selected.Online
                    });
                }
                diaData.Categories.Add(category);
            }
            return diaData;
        }

        public void ensureCreated()
        {
            try
            {
                _bdContext.Database.Migrate();
            }
            catch (Exception e)
            {
                _logger.LogWarning("Maybe harmless, but {0}",e.Message);
            }
            
        }
    }

    public class DCData
    {
        public string User { get; set; }
        [Key]public DateTime Timestamp { get; set; }
        public int Online { get; set; }
    }
}