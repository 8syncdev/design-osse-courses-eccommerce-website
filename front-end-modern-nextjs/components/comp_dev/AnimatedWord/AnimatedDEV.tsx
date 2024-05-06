"use client"
import React from 'react'
import dynamic from "next/dynamic";

const AnimatedModule = dynamic(
    () => {
        return import("react-animated-numbers");
    },
    { ssr: false }
);

const AnimatedAT = ({
    value = 5,
    duration = 0.5
}: {
    value?: number,
    duration?: number
}) => {
    return (
        <>
            <AnimatedModule
                includeComma
                animateToNumber={value}
                locale="en-US"
                className=""
                transitions={(_) => ({
                    type: "tween",
                    duration: duration,
                })}
            />
        </>
    )
}

export default AnimatedAT