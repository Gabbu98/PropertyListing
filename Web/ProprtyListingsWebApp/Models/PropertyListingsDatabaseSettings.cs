namespace ProprtyListingsWebApp.Models
{
    public class PropertyListingsDatabaseSettings
    {
        public string ConnectionString { get; set; } = null!;

        public string DatabaseName { get; set; } = null!;

        public string PropertiesCollectionName { get; set; } = null!;
    }
}
