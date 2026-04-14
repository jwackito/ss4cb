const sensitiveData = {
    apiKey: "12345-SECRET-KEY",
    dbPassword: "admin_password"
};

const accessProxy = new Proxy(sensitiveData, {
    get: (target, property) => {
        // Logging access and restricting specific fields
        console.log(`Accessing property: ${property}`);
        
        if (property === "dbPassword") {
            return "ACCESS DENIED";
        }
        
        return target[property];
    }
});
