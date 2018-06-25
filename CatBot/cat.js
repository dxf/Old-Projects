const Discord = require("discord.js");
const client = new Discord.Client();
client.on('ready', () => {
    console.log('Ready to rumble!');
});
client.on('message', (msg) => {
    if (msg.content === '+cat') {
        console.log('Someone requested a cat');
        msg.channel.send("Here you go", {
            file: new Discord.Attachment('https://lorempixel.com/500/500/cats/', 'cat.jpg')
        });
    } else if (msg.content === '+help') {
        msg.channel.send('There is one command. +cat. @yeahimdaf')
    }
});
client.login('Token here')
