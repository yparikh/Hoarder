import React, {useEffect, useState} from 'react'
import "beercss";
import "material-dynamic-colors";

const Header = () => {
    return (
        <header className="fill">
            <nav>
                <button className="circle transparent">
                    <i>menu</i>
                </button>
                <h5 className="max center-align">Hoarder</h5>
                <DarkModeButton/>
            </nav>
        </header>
    )
}

const DarkModeButton = () => {

    const [toggle, setToggle] = useState("light");

    const mode = () => {
      const newMode = window.ui("mode") === "dark"
          ? "light"
          : "dark";
      setToggle(window.ui("mode", newMode));
  }

    useEffect(() => {
        mode();
    })

    return (
        <label className="switch" onClick={()=> mode()}>
            <input type="checkbox"/>
            <span>
                <i>dark_mode</i>
            </span>
        </label>
    )
}


export default Header
