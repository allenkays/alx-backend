import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('Error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

/* Create Hash */
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

/* Display Hash */
client.hgetall('HolbertonSchools', (error, object) => {
  if (error) {
    console.error(`Error retrieving hash: ${error}`);
  } else {
    console.log(object);
  }
});

/* Gracefully handle process exit */
process.on('SIGINT', () => {
  client.quit();
  process.exit();
});
