const client = createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server')})
  .on('error', (err) => {
        console.error('Redis client not connected to the server:', err.message)})

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        redis.print(`Reply ${reply}`);
    });
}
          
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");