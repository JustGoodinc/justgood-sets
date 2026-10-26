@echo off
rem Starts JustGood Sets on this computer so Chrome can talk to a DDJ-FLX4.
rem Web MIDI only works on a local address or https, so this runs a small local web server.
rem Close this window to stop it.
cd /d "%~dp0"
set PORT=8790
title JustGood Sets (close this window to stop)
where py >nul 2>nul
if errorlevel 1 (
  echo Python is needed to run the local server. Install it from https://www.python.org/downloads/ and try again.
  pause
  exit /b 1
)
rem Open Chrome (or Edge if Chrome isn't installed) once the server is up
start "" /b cmd /c "timeout /t 1 >nul & (start chrome http://localhost:%PORT%/ || start msedge http://localhost:%PORT%/)"
echo JustGood Sets is running at http://localhost:%PORT%/
echo Keep this window open while you play. Close it to stop.
py -m http.server %PORT% --bind 127.0.0.1
