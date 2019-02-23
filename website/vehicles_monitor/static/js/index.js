$(function(){
    //Build Tabulator
    var table = new Tabulator("#vehicles-table", {
        //height:"311px",
        layout:"fitColumns",
        placeholder:"No Data Set",
        columns:[
            {title:"ID", field:"id", sorter:"string", headerFilter:"input"},
            {title:"Reg.nr", field:"reg_nr", sorter:"string", headerFilter:"input"},
            {title:"Owner Name", field:"owner_name", sorter:"string", headerFilter:"input"},
            {title:"Owner address", field:"owner_address", sorter:"string", headerFilter:"input"},
            {title:"Status", field:"up", align:"center", formatter:"tickCross", sorter:"boolean",  headerFilter:"tickCross",
              headerFilterParams:{"tristate":true},headerFilterEmptyCheck:function(value){return value === null}}
        ],
    });
    // load initial data
    table.setData("/vehicles");
    // then reload every 1 min
    setInterval(function(){
        table.setData("/vehicles");
        console.log("reloading...")
    }, 60000)

})