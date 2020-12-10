const path = require('path');
const fs = require('fs');

const defaultFolder = './record';
const copiesFolder = './copies';
const fileExt = "mp4";
let baseFolder = '';

const checkOld = () =>{
    if (fs.existsSync(copiesFolder)){
        return true;
    } return false;
}

const checkDefault = () => {
    if (fs.existsSync(defaultFolder)){
        return true;
    } return false;
}

// check to see if user has specifyed a folder
if (process.argv[2]){
    console.log(`Checking for folder... ${process.argv[2]}`)
    if (fs.existsSync(process.argv[2])){
        console.log(`${process.argv[2]} Located!`);
        baseFolder = process.argv[2];
    } else if (process.argv[2] && process.argv[2] != undefined) {
        // if user has but the folder is not found return error
        console.error(`${process.argv[2]} was not found, exiting`)
        process.exit();
    }
}

// if the user has not specifyed folder, check for default folder
if (!checkOld()){
    //check if old folder exists
    if (baseFolder === ''){
        if (checkDefault()){
            baseFolder = defaultFolder
        } else {
            console.error('record folder was not found in this directory');
            process.exit()
        }
    }
} else {
    console.error('copies folder located, please rename or remove');
    console.warn('This is implemented to prevent overwriting your old files');
    process.exit()
}

const listOfFileDirs = [];

for (let day of fs.readdirSync(baseFolder)){
    for (let hour of fs.readdirSync(path.join(baseFolder, day))){
        for (let minute of fs.readdirSync(path.join(baseFolder, day, hour))){
            if (minute && minute.split('.')[1] == fileExt){
            listOfFileDirs.push(path.join(baseFolder, day, hour, minute))
            }
        }
    }
}

if (listOfFileDirs){
    let count = 1;
    fs.mkdir('copies', (error)=>{
        if (error){
        console.log(error)
        }
    });

    listOfFileDirs.map(dir=>(
        fs.copyFile(
                dir,
                `./copies/${count++}.${fileExt}`,
                fs.constants.COPYFILE_EXCL,
                (err)=>{
            if (err){
            console.log(err)
            }
          })
        ));
} else {
    console.log('folders found but no content');
}

