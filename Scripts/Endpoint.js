
/**
 *  Simple fileserver to simulate a schema endpoint.
 * 
 *  When testing you can use any pathname to force 
 *  the xml language server to re-fetch the schema.
 */


const file = Bun.file('./.build/Schema.xsd')


const server = Bun.serve({

    port : 3000 ,

    async fetch (){
        
        const xsd = await file.text()
        
        const response = new Response(xsd)
        response.headers.set('Content-Type','application/xml')

        return response
    }
})

console.log(`Listening on ${ server.url }`)