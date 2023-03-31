import {createClient, print} from 'redis';

const client = createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function(err) {
  console.log('Redis client not connected to the server: ' + err)
});

const data = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
};

Object.keys(data).forEach((key) => {
  client.hset('HolbertonSchools', key, data[key], print);
});

client.hgetall('HolbertonSchools', (err, val) => {
  console.log(JSON.stringify(val));
});
