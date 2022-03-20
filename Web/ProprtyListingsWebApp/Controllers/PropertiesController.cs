using Microsoft.AspNetCore.Mvc;
using ProprtyListingsWebApp.Models;
using ProprtyListingsWebApp.Services;

namespace ProprtyListingsWebApp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PropertiesController : ControllerBase
    {
        private readonly PropertiesService _propertiesService;

        public PropertiesController(PropertiesService propertiesService)
        {
            _propertiesService = propertiesService;
        }

        [HttpGet]
        public async Task<List<Property>> Get() => await _propertiesService.GetAsync();
    }
}
