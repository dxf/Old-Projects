const Discord = require("discord.js");
const self = new Discord.Client(); 

self.on('ready', () => {
console.log(`Logged in as ${self.user.tag}!`);
self.user.setActivity('A cool game', {url: 'https://twitch.tv/placeholder', type: 'STREAMING'});
)};

self.login('token');

//Credit to @LumiteDubbz for this, but this is how you make your status purple in JavaScript 
