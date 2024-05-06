'use server'
import { CacheType, OptionType } from '@/types'
const post = async (url: string, body: any, options: OptionType = {}, cache: CacheType='default') => {
    /*
        * Post actions
    */
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                ...options
            },
            body: JSON.stringify(body),
            cache: cache,
        })
        const data = await response.json()
        return data
    } catch (error) {
        console.error(error)
    }
}

export default post