'use client'
import { usePathname } from 'next/navigation'
import React from 'react'
// import tokenService from '../server/service/token.action'
import SelectDEV from '@/components/shared/SelectShared/SelectShared'
import userService from '../server/service/user.action'
// import { useParams } from 'next/navigation'
// import { useSearchParams } from 'next/navigation'

const AuthAvatarProvider = ({
    children,
    params,
    searchParams
}: {
    children: React.ReactNode,
    params?: any,
    searchParams?: any
}) => {
    const [allow, setAllow] = React.useState<boolean>(false)
    const [data, setData] = React.useState<any>({})
    const pathName = usePathname()

    try {
        const data = localStorage.getItem('authToken') as string;
        var authToken = data
    }
    catch (error) {
        var authToken = ''
    }

    React.useEffect(() => {
        const fetchAuth = async () => {
            if (authToken && authToken !== '' && data?.data?.username === undefined) {
                // console.log(authToken)
                const data = await userService.getProfile({
                    'Authorization': `JWT ${authToken}`
                })
                // console.log(data)
                if (data && data?.code === 'res_success') {
                    setAllow(true)
                    setData(data)
                }
            }
            else {
                setAllow(false)
            }
        }
        if (authToken !== '')
            fetchAuth()
    }, [authToken])

    return (
        <>
            {(!allow) ? children : <>
                <SelectDEV placeholder={data && data.data.username} items={[]} />
            </>}
        </>
    )
}

export default AuthAvatarProvider