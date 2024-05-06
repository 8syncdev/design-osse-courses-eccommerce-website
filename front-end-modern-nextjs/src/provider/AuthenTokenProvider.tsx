'use client'
import { usePathname } from 'next/navigation'
import React, { use, useEffect } from 'react'
import tokenService from '../server/service/token.action'
import LoadingBar from '@/components/comp_dev/LoadingStateDEV/LoadingBar'
import { set } from 'zod'
// import { useParams } from 'next/navigation'
// import { useSearchParams } from 'next/navigation'

const AuthenTokenProvider = ({
    children,
    params,
    searchParams
}: {
    children: React.ReactNode,
    params?: any,
    searchParams?: any
}) => {
    const [allow, setAllow] = React.useState<boolean>(false)
    const [isLoading, setIsLoading] = React.useState<boolean>(false)
    const [data, setData] = React.useState<any>({})
    const pathName = usePathname()

    try {
        const data = localStorage.getItem('authToken') as string;
        var authToken = data
    }
    catch (error) {
        var authToken = ''
    }


    useEffect(() => {
        const fetchAuth = async () => {
            if (authToken && authToken !== '') {
                // console.log(authToken)
                setIsLoading(true)
                const data = await tokenService.checkTokenValid({
                    'Authorization': `JWT ${authToken}`
                })
                /**
                 * * Use data to check if the token is valid, if the token is valid, setAllow to true, else setAllow to false, LoadingBar will be shown until the data is fetched
                 */
                if (data && data?.code === 'res_success') {
                    setAllow(true)
                    setIsLoading(false)
                }
                else {
                    setAllow(false)
                    setIsLoading(false)
                }
            }
            else {
                setAllow(false)
                setIsLoading(false)
            }
        }
        if (authToken !== '')
            fetchAuth()
        else{
            setAllow(false)
            setIsLoading(false)
        }
    }, [authToken, pathName])


    // * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    const listIDLessonAllow = [...Array.from({ length: 28 }, (_, i) => `${i + 1}`)]
    // console.log(searchParams)
    return (
        <>
            {!isLoading ?
                ((allow ||
                    listIDLessonAllow.includes(searchParams?.id)
                ) ? children : <>
                    <div className='h-full w-full flex justify-center pt-20'>
                        <div className='text-2xl'>Vui lòng liên hệ 0703930513</div>
                    </div>
                </>) : <>
                    <LoadingBar />
                </>
            }
        </>
    )
}

export default AuthenTokenProvider