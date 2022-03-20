using MongoDB.Bson.Serialization.Attributes;

namespace ProprtyListingsWebApp.Models
{
    public class Property
    {
        [BsonId]
        [BsonRepresentation(MongoDB.Bson.BsonType.ObjectId)]
        public string? Id { get; set; }

        [BsonElement("Type")]
        public string Type { get; set; } = null!;

        public double Cost { get; set; }

        public string Location { get; set; } = null;

    }
}
