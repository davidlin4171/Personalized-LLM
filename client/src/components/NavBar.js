import React from "react";
import { NavLink, useNavigate } from "react-router-dom";

function NavBar() {
  const navigate = useNavigate();
  const user = localStorage.getItem("user");

  const linkClass =
    "px-4 py-2 rounded hover:bg-blue-100 transition text-sm font-medium";

  const activeClass = "bg-black text-white";

  const handleLogout = () => {
    localStorage.removeItem("user");
    navigate("/login");
  };

  return (
    <nav className="bg-white shadow p-4 flex justify-end gap-4">
      {!user && (
        <NavLink
          to="/login"
          className={({ isActive }) =>
            `${linkClass} ${isActive ? activeClass : ""}`
          }
        >
          Login
        </NavLink>
      )}
      <NavLink
        to="/chat"
        className={({ isActive }) =>
          `${linkClass} ${isActive ? activeClass : ""}`
        }
      >
        Chat
      </NavLink>
      <NavLink
        to="/profile"
        className={({ isActive }) =>
          `${linkClass} ${isActive ? activeClass : ""}`
        }
      >
        Account
      </NavLink>

      {user && (
        <button
          onClick={handleLogout}
          className={linkClass}
        >
          Log out
        </button>
      )}
    </nav>
  );
}

export default NavBar;
