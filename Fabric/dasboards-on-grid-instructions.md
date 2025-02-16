# Instructions Dasboards on Grid


```bash
fabric -y https://www.youtube.com/watch?v=5gPSsZ9MXkE -o ../../../working/foamy-stuff/Fabric/dasboards-on-grid-instructions.md -p extract_instructions
```

## Objectives
- Learn to create and customize dashboards in Home Assistant using Lovelace.
- Understand how to set up dedicated devices for displaying dashboards.
- Utilize add-ons like Browser Mod and Layout Card for enhanced dashboard functionality.

### Instructions
1. **Set Up Dedicated Devices:**
   - Look for affordable touchscreens or tablets on resale markets like Facebook Marketplace or Kijiji.
   - Consider Microsoft Surface devices, especially the desktop versions, for their touchscreen capabilities.
   - Alternatively, use inexpensive tablets or touchscreen devices available on Amazon.

2. **Install Necessary Add-ons:**
   - Use HACS (Home Assistant Community Store) to install Browser Mod and Layout Card.
   - Browser Mod allows control over each browser independently.
   - Layout Card provides flexibility in arranging cards within a Lovelace dashboard.

3. **Create a New Dashboard:**
   - Go to your Home Assistant interface and create a new dashboard or tab.
   - Name it (e.g., "Demo Dashboard") and choose "Panel" for the view type.

4. **Add a Layout Card:**
   - Add a card to the dashboard and search for "Layout."
   - Select "Custom Layout Card" and choose "Grid" for the layout type.
   - Save the settings.

5. **Define the Grid:**
   - Edit the dashboard and define the grid template columns and rows.
   - Example: Columns: 240, 240, 240, 240, 240, 240, 240, 240; Rows: 110, 256, 256, 256, 196.
   - Assign names to each grid cell for easy identification (e.g., Row1Col1, Row1Col2, etc.).

6. **Add Controls to the Grid:**
   - Add a card (e.g., a switch for "Globe Light") to the dashboard.
   - Edit the card and add the view layout and grid area (e.g., Row1Col5).
   - Save the changes to see the card move to the specified grid location.

7. **Customize Card Placement:**
   - Add more cards and assign them to specific grid areas.
   - Adjust the pixel density of rows to change the size of the cards.
   - Combine row and column names to stretch cards across multiple rows or columns.

8. **Experiment with Layout:**
   - Add or remove rows and columns to fine-tune the dashboard layout.
   - Use the code editor to make precise adjustments to the grid and card placements.

9. **Utilize New Features:**
   - Upgrade Home Assistant to access new dashboard functionalities.
   - Look forward to easier drag-and-drop features for creating dashboards.

10. **Subscribe and Engage:**
    - Consider subscribing to the channel for more Home Assistant tips.
    - Give the video a thumbs up if found helpful.