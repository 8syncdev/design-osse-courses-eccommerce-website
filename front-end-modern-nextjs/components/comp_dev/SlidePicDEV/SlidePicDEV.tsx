import React, { memo } from 'react'
import './style.css'
// Images Tech:
import { nestjsplainImg, javascriptoriginalImg, tailwindcssoriginalwordmarkImg, html5originalwordmarkImg, css3originalImg, typescriptoriginalImg, reactoriginalImg, mysqloriginalImg, sassoriginalImg, sequelizeoriginalImg } from '@/src/constant/image'
//
import Image, { StaticImageData } from 'next/image'



const SlidePicDEV = ({
    listImgProps = [
        nestjsplainImg, javascriptoriginalImg, tailwindcssoriginalwordmarkImg, html5originalwordmarkImg, css3originalImg, typescriptoriginalImg, reactoriginalImg, mysqloriginalImg, sassoriginalImg, sequelizeoriginalImg
    ]
}: {
    listImgProps?: StaticImageData[]
}) => {
    const listImg = listImgProps
    return (
        <div className="slider">
            <div className="rotator">
                {listImg.map((item, index) => {
                    return <div key={index} className="items grid place-items-center p-3 lg:w-[4rem] w-2rem">
                        <Image src={item} alt='' className=''/>
                    </div>
                })}

            </div>
        </div>
    )
}

export default memo(SlidePicDEV)