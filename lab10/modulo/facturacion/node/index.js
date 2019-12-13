var Odoo = require("odoo-xmlrpc");

var odoo = new Odoo({
    url: "localhost",
    port: 8069,
    db: "db_labse",
    username: "admin",
    password: "admin"
});

odoo.connect(function(err){
    if (err){
        return(console.log(err,"aea"));
    }
    console.log("Conectado al servicio de Odoo");
    var inParams = [];
    inParams.push([]);
    var params = [];
    params.push(inParams);
    odoo.execute_kw("facturacion.series","search_read",params, function(
        err,
        value
    ){
        if(err){
            return console.log(err,"mongol");
        }
        console.log("Result: ", value);
    });
});