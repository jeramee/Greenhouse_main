function ls_function(error, stdout, stderr) 
{
    const { exec } = require('child_process');

    if (error) {
        console.error(`exec error: ${error}`);
        return;
    }
    if (stderr) {
        console.error(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
}
    
    