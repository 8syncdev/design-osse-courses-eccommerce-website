"use client"
import React from 'react'
import { TypeAnimation } from 'react-type-animation';


const TypeWriterDEV = ({
    classWrapper = '',
    className = '',
    sequence = [
        "Không Biết Bắt Đầu Từ Đâu?",
        2000,
        "Học Ngôn Ngữ Lập Trình Nào?",
        2000,
        "Cách Học Hiệu Quả Nhất?",
        2000,
        "Chi Phí Ít Tốn Kém?",
        2000,
    ]
}:
    {
        classWrapper?: string,
        className?: string,
        sequence?: any[]
    }) => {
    return (
        <div className={`mb-5 ${classWrapper}`}>
            <TypeAnimation className={`${className}`}
                sequence={sequence}
                wrapper="span"
                speed={30}
                repeat={Infinity}
                style={{}}

            />
        </div>
    )
}

export default TypeWriterDEV