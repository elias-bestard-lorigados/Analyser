const { dialog } = require('electron').remote
const Highcharts = require('highcharts');
function load_html() {
    dialog.showOpenDialog((fileNames) => {
        // fileNames is an array that contains all the selected
        if (fileNames === undefined) {
            console.log("No file selected");
            return;
        }
        html_path = fileNames[0].replace(/ /g, "%20");
        $('.menuContainer').load(html_path);
        // document.getElementById('modify_db_bttn').style.visibility="visible";
    });
}