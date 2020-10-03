using System;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace DCTracker.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class BugsController : ControllerBase
    {
        private readonly IDbConnect _dbc;
        private readonly ILogger _logger;
        private readonly IConfiguration _configuration;

        public BugsController(IDbConnect dbc, ILogger<BugsController> logger,IConfiguration configuration)
        {
            _configuration = configuration;
            _dbc = dbc;
            _logger = logger;
        }

        // GET: api/<BugsController>
        [HttpGet]
        public IActionResult Get()
        {
            string num = HttpContext.Request.Query["limit"].ToString();
            int lines;
            if (int.TryParse(num, out lines))
            {
                _logger.LogInformation("{0} Line Diagram Data is requested", lines);
            }
            else
            {
                _logger.LogInformation("Line value missing defaulting to settings val");
                lines = int.Parse(_configuration["FetchOptions:DataCap"]);
            }

            if (lines < 1)
            {
                _logger.LogInformation("Line value to low defaulting to settings val");
                lines = int.Parse(_configuration["FetchOptions:DataCap"]);
            }

            try
            {
                var res = Ok(_dbc.GetDiaData(lines));
                _logger.LogInformation("Diagram Data is returned");
                return res;
            }
            catch (Exception ex)
            {
                var res = Problem(ex.Message);
                _logger.LogWarning("Diagram Data is not returned, because of {0}", ex.Message);
                return res;
            }
        }
    }
}