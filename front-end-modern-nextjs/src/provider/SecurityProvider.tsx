'use client'
import React, { useEffect } from 'react'






const buildPreventKey = () => {
    document.addEventListener('contextmenu', event => event.preventDefault());

    document.onkeydown = function (e) {

        // disable F12 key
        if (e.keyCode == 123) {
            return false;
        }

        // disable I key
        if (e.ctrlKey && e.shiftKey && e.keyCode == 73) {
            return false;
        }

        // disable J key
        if (e.ctrlKey && e.shiftKey && e.keyCode == 74) {
            return false;
        }

        // disable U key
        if (e.ctrlKey && e.keyCode == 85) {
            return false;
        }
    }
}

const SecurityProvider = ({
    children,
    onSecurity=true
}: {
    children: React.ReactNode
    onSecurity?: boolean
}) => {
    /**
     * * Solve this issue by using useEffect to build the prevent key
     */
    useEffect(()=>{
        onSecurity && buildPreventKey()
    }, [])
    return (
        <>
            {children}
        </>
    )
}

export default SecurityProvider