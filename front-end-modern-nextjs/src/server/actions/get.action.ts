'use server'
import { CacheType, OptionType } from '@/types'
const get = async (url: string, options: OptionType = {}, cache: CacheType ='default') => {
    /*
        * Get actions
    */
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                ...options
            },
            cache: cache,
        })
        const data = await response.json()
        return data
    } catch (error) {
        console.error(error)
    }
}

export default get