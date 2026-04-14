const datosSensibles = {
    llaveApi: "12345-LLAVE-SECRETA",
    contraseniaBd: "admin_contrasenia"
};

const proxyDeAcceso = new Proxy(datosSensibles, {
    get: (objetivo, propiedad) => {
        //Acceso de Login y restriccion de campos especificos
        console.log(`Accediendo pripiedad: ${propiedad}`);
        
        if (propiedad === "contraseniaBd") {
            return "Acceso Denegado";
        }
        
        return objetivo[propiedad];
    }
});
