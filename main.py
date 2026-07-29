from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform
from kivy.clock import mainthread

class LocationApp(App):
    def build(self):
        # Main layout with spacing and padding
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Header Label
        self.title_label = Label(
            text="Kivy GPS Tracker", 
            font_size='28sp', 
            bold=True,
            size_hint_y=0.2,
            color=(0.1, 0.6, 0.8, 1) # Cyan-blue color
        )
        self.layout.add_widget(self.title_label)
        
        # Status & Coordinates Display Area
        self.status_label = Label(
            text="Status: Ready\nClick the button to request location permissions and start tracking.",
            font_size='18sp',
            halign='center',
            valign='middle',
            size_hint_y=0.5
        )
        # Bind text size to label size to allow proper wrapping
        self.status_label.bind(size=self.status_label.setter('text_size'))
        self.layout.add_widget(self.status_label)
        
        # Primary Action Button
        self.action_button = Button(
            text="Get Geolocation",
            font_size='20sp',
            size_hint_y=0.3,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        self.action_button.bind(on_press=self.on_button_click)
        self.layout.add_widget(self.action_button)
        
        # Lifecycle / state flags
        self.gps_active = False
        self.gps_configured = False
        
        return self.layout
        
    def on_button_click(self, instance):
        if platform == 'android':
            self.check_and_request_permissions()
        else:
            self.status_label.text = "Platform is not Android.\nSimulating location update..."
            self.simulate_location()

    def check_and_request_permissions(self):
        from android.permissions import check_permission, Permission
        
        fine_loc = Permission.ACCESS_FINE_LOCATION
        coarse_loc = Permission.ACCESS_COARSE_LOCATION
        
        # Check if permissions are already granted
        if check_permission(fine_loc) and check_permission(coarse_loc):
            self.status_label.text = "Permissions already granted.\nStarting GPS..."
            self.start_gps()
        else:
            self.status_label.text = "Requesting location permissions..."
            from android.permissions import request_permissions
            request_permissions([fine_loc, coarse_loc], self.permission_callback)

    def permission_callback(self, permissions, results):
        if all(results):
            self.status_label.text = "Permissions granted!\nStarting GPS..."
            self.start_gps()
        else:
            self.status_label.text = "Error: Geolocation permissions denied.\nPlease grant permissions in Android settings."
            print("Permissions were denied by the user.")

    def start_gps(self):
        if self.gps_active:
            self.stop_gps()
            return
            
        try:
            from plyer import gps
            if not self.gps_configured:
                gps.configure(on_location=self.on_location, on_status=self.on_status)
                self.gps_configured = True
            
            # Start updates every 1 second or 1 meter
            gps.start(minTime=1000, minDistance=1)
            self.gps_active = True
            self.action_button.text = "Stop GPS Tracking"
            self.status_label.text = "GPS tracking active. Waiting for signal..."
            print("GPS started successfully.")
        except Exception as e:
            self.status_label.text = f"Failed to start GPS:\n{str(e)}"
            print(f"Exception while starting GPS: {e}")

    def stop_gps(self):
        if not self.gps_active:
            return
        try:
            from plyer import gps
            gps.stop()
            self.gps_active = False
            self.action_button.text = "Get Geolocation"
            self.status_label.text = "GPS tracking stopped."
            print("GPS stopped.")
        except Exception as e:
            print(f"Exception while stopping GPS: {e}")

    @mainthread
    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        altitude = kwargs.get('altitude', 0.0)
        
        # Update the UI
        self.status_label.text = (
            f"Location Updated!\n\n"
            f"Latitude: {lat}\n"
            f"Longitude: {lon}\n"
            f"Altitude: {altitude}m"
        )
        
        # Print coordinates as requested
        print(f"Lat: {lat}, Lon: {lon}")

    @mainthread
    def on_status(self, stype, status):
        print(f"Status update: {stype} - {status}")
        self.status_label.text = f"GPS Status: {status}\nWaiting for location fix..."

    def simulate_location(self):
        # Simulated geolocation for testing on non-Android platforms
        import random
        lat = round(random.uniform(-90.0, 90.0), 6)
        lon = round(random.uniform(-180.0, 180.0), 6)
        self.on_location(lat=lat, lon=lon)

    def on_pause(self):
        # Stop GPS to conserve battery when app goes into background
        if self.gps_active:
            self.stop_gps()
            self.gps_active = True # keep flag True so it resumes automatically
        return True

    def on_resume(self):
        # Restart GPS when app returns to foreground
        if self.gps_active:
            self.gps_active = False # Reset flag to allow starting GPS again
            self.start_gps()

if __name__ == '__main__':
    # Buildozer configurations to remember:
    # ------------------------------------
    # In buildozer.spec:
    # requirements = python3, kivy, plyer
    # android.permissions = ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION
    # ------------------------------------
    LocationApp().run()