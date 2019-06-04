const loadJsonFile = require('load-json-file');
const writeJsonFile = require('write-json-file');

function modify_db() {
    dialog.showOpenDialog((fileNames) => {
        // fileNames is an array that contains all the selected
        if (fileNames === undefined) {
            console.log("No file selected");
            return;
        }
        html_path = fileNames[0].replace(/ /g, "%20");
        // document.getElementById('modify_db_bttn').style.visibility = "visible";
        var filepath = "./utils/data_base.json";
        var filepath = html_path;
        var c = Array.from(document.getElementsByTagName('INPUT')).filter(cur => cur.type == 'checkbox');
        var json_obj=loadJsonFile.sync(filepath);
        console.log(c);
        for (i in c){
            for(j in json_obj){
                if (json_obj[j]['id']==c[i].id) {
                    json_obj[j]['useful'] = c[i].checked;
                }
            }
        }
        console.log(json_obj);
        writeJsonFile.sync(filepath, json_obj);
        alert('Se actualizo al base de datos satisfactoriamente');
    });
}