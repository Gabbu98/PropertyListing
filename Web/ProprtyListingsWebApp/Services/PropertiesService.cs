using Microsoft.Extensions.Options;
using MongoDB.Driver;
using ProprtyListingsWebApp.Models;

namespace ProprtyListingsWebApp.Services
{
    public class PropertiesService
    {
        private readonly IMongoCollection<Property> _propertiesCollection;

        public PropertiesService ( IOptions<PropertyListingsDatabaseSettings> propertyListingDatabaseSettings )
        {
            var mongoClient = new MongoClient(
               propertyListingDatabaseSettings.Value.ConnectionString);

            var mongoDatabase = mongoClient.GetDatabase(
                propertyListingDatabaseSettings.Value.DatabaseName);

            _propertiesCollection = mongoDatabase.GetCollection<Property>(
                propertyListingDatabaseSettings.Value.PropertiesCollectionName);
        }

        public async Task<List<Property>> GetAsync() =>
       await _propertiesCollection.Find(_ => true).ToListAsync();

        public async Task<Property?> GetAsync(string id) =>
            await _propertiesCollection.Find(x => x.Id == id).FirstOrDefaultAsync();

        public async Task CreateAsync(Property newProperty) =>
            await _propertiesCollection.InsertOneAsync(newProperty);

        public async Task UpdateAsync(string id, Property updatedProperty) =>
            await _propertiesCollection.ReplaceOneAsync(x => x.Id == id, updatedProperty);

        public async Task RemoveAsync(string id) =>
            await _propertiesCollection.DeleteOneAsync(x => x.Id == id);
    }
}
