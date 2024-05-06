import React from 'react'

const AvatarDEV = async ({
    token,
    children
}: {
    token?: string,
    children?: React.ReactNode
}) => {
    console.log(token)
    return (
        <div>
            {children}
        </div>
    )
}

export default AvatarDEV