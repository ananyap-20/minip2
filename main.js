const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { PythonShell } = require('python-shell');
const express = require('express');
const server = express();

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.loadFile('index.html');
  mainWindow.webContents.openDevTools();
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// Handle debug session
let pyshell = null;

ipcMain.on('start-debug', (event, { filePath, breakpoints }) => {
  if (pyshell) {
    pyshell.end();
  }

  pyshell = new PythonShell('debugger.py', {
    mode: 'json',
    args: [filePath, JSON.stringify(breakpoints)]
  });

  pyshell.on('message', (message) => {
    mainWindow.webContents.send('debug-update', message);
  });

  pyshell.on('error', (err) => {
    mainWindow.webContents.send('debug-error', err.message);
  });
});

ipcMain.on('debug-command', (event, command) => {
  if (pyshell) {
    pyshell.send(command);
  }
});

// Start Express server for web interface
server.use(express.static(path.join(__dirname, 'web')));
server.listen(3000, () => {
  console.log('Web interface available at http://localhost:3000');
});