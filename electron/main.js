const { app, BrowserWindow, Menu } = require("electron");
const path = require("path");
function createWindow() {
  const win = new BrowserWindow({
    width: 1100, height: 760, minWidth: 380, minHeight: 600,
    title: "Savdo Hisobi", icon: path.join(__dirname, "icon.ico"),
    backgroundColor: "#f3f5f4",
    webPreferences: { contextIsolation: true, sandbox: true }
  });
  Menu.setApplicationMenu(null);
  win.loadFile(path.join(__dirname, "..", "www", "index.html"));
}
const lock = app.requestSingleInstanceLock();
if (!lock) app.quit();
else {
  app.whenReady().then(createWindow);
  app.on("window-all-closed", () => app.quit());
}
