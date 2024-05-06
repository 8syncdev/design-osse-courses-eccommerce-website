import React from 'react'

const LoadingBar = ({
    number_bar = 10,
    sizeHeight = 50
}: {
    number_bar?: number,
    sizeHeight?: number
}) => {
    return (
        <>
            <div className='neon-loading'>
                {Array.from({ length: number_bar }).map((_, index: number) => {
                    return <div key={index} className={`neon-pulse mb-4 h-[${sizeHeight}px]`} />
                })}
            </div>
        </>
    )
}

export default LoadingBar