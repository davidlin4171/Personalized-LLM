import React, { useState } from "react";

function ProfilePage() {
  const [userInfo, setUserInfo] = useState({
    name: "",
    email: "",
    gender: "",
    location: "",
    occupation: "",
    interests: []
  });

  const [editMode, setEditMode] = useState(false);
  const [draftInfo, setDraftInfo] = useState(null); // draft

  const handleChange = (key, value) => {
    setUserInfo((prev) => ({ ...prev, [key]: value }));
  };

  const handleSave = () => {
    // TODO: save to database

    setUserInfo(draftInfo);
    setEditMode(false);
    setDraftInfo(null);
    alert("Information saved");
  };

  const handleCancel = () => {
    setDraftInfo(null); // discard draft
    setEditMode(false);
  };

  const displayData = editMode ? draftInfo : userInfo;

  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center p-6">
      <div className="bg-white shadow-md rounded p-6 w-full max-w-lg space-y-4">
        <h2 className="text-2xl font-bold">Personal info</h2>

        <div className="space-y-2">
          <label className="block text-sm font-medium">Name</label>
          <input
            disabled={!editMode}
            value={editMode ? draftInfo?.name : userInfo.name}
            onChange={(e) => editMode && setDraftInfo({ ...draftInfo, name: e.target.value })}

            className="w-full border px-3 py-2 rounded"
          />

          <label className="block text-sm font-medium">Email</label>
          <input
            disabled={!editMode}
            value={editMode ? draftInfo?.email : userInfo.email}
            onChange={(e) => editMode && setDraftInfo({ ...draftInfo, email: e.target.value })}

            className="w-full border px-3 py-2 rounded"
          />

          <label className="block text-sm font-medium">Gender</label>
          <input
            disabled={!editMode}
            value={editMode ? draftInfo?.gender : userInfo.gender}
            onChange={(e) => editMode && setDraftInfo({ ...draftInfo, gender: e.target.value })}

            className="w-full border px-3 py-2 rounded"
          />

          <label className="block text-sm font-medium">Location</label>
          <input
            disabled={!editMode}
            value={editMode ? draftInfo?.location : userInfo.location}
            onChange={(e) => editMode && setDraftInfo({ ...draftInfo, location: e.target.value })}

            className="w-full border px-3 py-2 rounded"
          />

          <label className="block text-sm font-medium">Occupation</label>
          <input
            disabled={!editMode}
            value={editMode ? draftInfo?.occupation : userInfo.occupation}
            onChange={(e) => editMode && setDraftInfo({ ...draftInfo, occupation: e.target.value })}
            
            className="w-full border px-3 py-2 rounded"
          />

          <label className="block text-sm font-medium">Interests</label>
          <input
            disabled={!editMode}
            value={editMode ? draftInfo?.interests?.join(", ") || "" : userInfo.interests.join(", ")
            }
            onChange={(e) => editMode && setDraftInfo({...draftInfo, interests: e.target.value.split(",").map((i) => i.trim()),})}

            className="w-full border px-3 py-2 rounded"
          />
        </div>

        <div className="pt-4 flex justify-end space-x-2">
          {editMode ? (
            <>
              <button
                className="px-4 py-2 bg-gray-300 rounded"
                onClick={handleCancel}
              >
                Cancel
              </button>
              <button
                className="px-4 py-2 bg-black text-white rounded hover:bg-gray"
                onClick={handleSave}
              >
                Save
              </button>
            </>
          ) : (
            <button
              className="px-4 py-2 bg-black text-white rounded hover:bg-gray"
              onClick={() =>  {
                setDraftInfo({ ...userInfo });
                setEditMode(true);
              }}
            >
              Edit
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

export default ProfilePage;
