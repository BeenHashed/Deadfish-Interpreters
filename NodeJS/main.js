const fs = require("fs");

const file = process.argv[2];
try {
    var code = fs.readFileSync(file, "utf-8")
} catch(e) { 
    console.log("File not found");
    process.exit(1);
}

let accumulator = 0;

for(let i of code) {
    if(accumulator >= 256 || accumulator < 0) accumulator = 0;

    switch(i) {
        case "i":
            accumulator++;
            break;
        case "d":
            accumulator--;
            break;
        case "s":
            accumulator *= accumulator;
            break;
        case "o":
            process.stdout.write(`${accumulator} `);
    }
}