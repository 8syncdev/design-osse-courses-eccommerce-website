import { ROUTE_LITERAL_TYPE } from "@/types"
import { API_BE_SSR } from "../actions/const"


const buildRoute = (route: ROUTE_LITERAL_TYPE, pk: string | null=null, custom_segment:string='') => {
    /**
     * * This function is used to build the route for the API
     * * Process work in SSR only so Env will give NULL in CSR
     */
    const DOMAIN_BE_FOR_CSR = "https://8sync-be-dev.vercel.app/pbkdf2_sha256390000jwfsotswr778gvfsh7wj7fnjacn7hmzwxfbd9cjxpabqqinw0ug2gvi494rrg8m"
    // const DOMAIN_BE_FOR_CSR = "http://127.0.0.1:8000/pbkdf2_sha256390000jwfsotswr778gvfsh7wj7fnjacn7hmzwxfbd9cjxpabqqinw0ug2gvi494rrg8m"
    if (process.env.VIEW_SET_NAME == null || process.env.VIEW_SET_NAME == undefined) {
        // console.log(process.env.VIEW_SET_NAME)
        return `${DOMAIN_BE_FOR_CSR}${route}${pk ? `${pk}/` : ''}${custom_segment}`

    }
    return `${API_BE_SSR}${route}${pk ? `${pk}/` : ''}${custom_segment}`
}

export default buildRoute