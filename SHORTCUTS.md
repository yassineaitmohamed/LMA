# ⌨️ Keyboard Shortcuts Reference

Complete guide to keyboard shortcuts in LMA PDF Reader Pro.

## 📖 Navigation

### Page Navigation
| Shortcut | Action |
|----------|--------|
| `→` or `Right Arrow` | Next page |
| `←` or `Left Arrow` | Previous page |
| `Space` | Scroll down / Next page |
| `Shift + Space` | Scroll up / Previous page |
| `Page Down` | Jump down multiple pages |
| `Page Up` | Jump up multiple pages |
| `Home` | Go to first page |
| `End` | Go to last page |
| `Ctrl + G` | Go to specific page (shows dialog) |

### Scroll Navigation
| Shortcut | Action |
|----------|--------|
| `↓` or `Down Arrow` | Scroll down |
| `↑` or `Up Arrow` | Scroll up |
| `Ctrl + Home` | Scroll to top of page |
| `Ctrl + End` | Scroll to bottom of page |

## 🔍 Search & Find

| Shortcut | Action |
|----------|--------|
| `Ctrl + F` | Open search dialog |
| `F3` or `Enter` | Find next occurrence |
| `Shift + F3` | Find previous occurrence |
| `Escape` | Close search / Clear highlights |
| `Ctrl + Shift + F` | Advanced search (case-sensitive) |

## 🖊️ Annotations

| Shortcut | Action |
|----------|--------|
| `Ctrl + H` | Toggle highlight mode |
| `Ctrl + N` | Add note at current position |
| `Ctrl + B` | Toggle bookmark for current page |
| `Ctrl + Shift + B` | Show all bookmarks |
| `Delete` | Delete selected annotation |
| `Ctrl + S` | Save all annotations |

### Highlight Colors
| Shortcut | Action |
|----------|--------|
| `1` | Yellow highlight |
| `2` | Green highlight |
| `3` | Blue highlight |
| `4` | Pink highlight |
| `5` | Orange highlight |

## 🎨 View & Display

### Zoom
| Shortcut | Action |
|----------|--------|
| `Ctrl + +` or `Ctrl + =` | Zoom in |
| `Ctrl + -` | Zoom out |
| `Ctrl + 0` | Reset zoom to 100% |
| `Ctrl + Scroll` | Zoom in/out with mouse wheel |

### Display Modes
| Shortcut | Action |
|----------|--------|
| `Ctrl + T` | Toggle dark/light theme |
| `F11` | Toggle fullscreen |
| `Ctrl + L` | Toggle thumbnails panel |
| `Ctrl + M` | Show/hide miniatures |
| `F5` | Presentation mode |

## 📤 Export & Tools

| Shortcut | Action |
|----------|--------|
| `Ctrl + E` | Export document (shows menu) |
| `Ctrl + P` | Print current page |
| `Ctrl + Shift + E` | Export annotations only |
| `Ctrl + C` | Copy selected text |
| `Ctrl + A` | Select all text on page |

### Export Formats (after Ctrl+E)
| Key | Format |
|-----|--------|
| `M` | Markdown |
| `T` | Plain text |
| `J` | JSON |
| `B` | BibTeX |
| `P` | PDF with annotations |

## 🤖 AI Tools

| Shortcut | Action |
|----------|--------|
| `Ctrl + 1` | Generate summary |
| `Ctrl + 2` | Extract key points |
| `Ctrl + 3` | Analyze content |
| `Ctrl + 4` | Extract citations |
| `Ctrl + 5` | Generate questions |

## 📊 Information & Help

| Shortcut | Action |
|----------|--------|
| `Ctrl + I` | Show document info |
| `Ctrl + Shift + I` | Show statistics |
| `F1` or `?` | Show this help |
| `Ctrl + R` | Reload document |
| `Ctrl + Q` | Quit application |

## 🔖 Bookmarks

| Shortcut | Action |
|----------|--------|
| `Ctrl + B` | Add/remove bookmark |
| `Ctrl + Shift + B` | Show bookmark list |
| `Ctrl + 1-9` | Jump to bookmark 1-9 |
| `Ctrl + Shift + 1-9` | Set quick bookmark 1-9 |

## 🎯 Advanced Features

### Selection & Copy
| Shortcut | Action |
|----------|--------|
| `Click + Drag` | Select text |
| `Ctrl + Click` | Select word |
| `Triple Click` | Select paragraph |
| `Ctrl + C` | Copy selection |
| `Ctrl + Shift + C` | Copy with citation |

### Thumbnail Navigation
| Shortcut | Action (when thumbnails visible) |
|----------|--------|
| `Tab` | Switch focus to thumbnails |
| `Arrow Keys` | Navigate thumbnails |
| `Enter` | Go to selected thumbnail page |
| `Delete` | (Reserved for future use) |

### Text Mode
| Shortcut | Action |
|----------|--------|
| `Ctrl + Shift + T` | Toggle text-only mode |
| `Ctrl + D` | Toggle dark reading mode |
| `Ctrl + [` | Decrease line spacing |
| `Ctrl + ]` | Increase line spacing |

## 🎮 Mouse Actions

### Basic Navigation
| Action | Result |
|--------|--------|
| `Click` | Move cursor |
| `Double Click` | Select word |
| `Triple Click` | Select paragraph |
| `Right Click` | Context menu |
| `Scroll Wheel` | Scroll page |
| `Ctrl + Scroll` | Zoom in/out |

### Advanced Selection
| Action | Result |
|--------|--------|
| `Click + Drag` | Select text |
| `Shift + Click` | Extend selection |
| `Ctrl + Click` | Add to selection |
| `Alt + Drag` | Rectangular selection |

### Annotation Actions
| Action | Result |
|--------|--------|
| `Click (highlight mode)` | Add highlight |
| `Right Click (on annotation)` | Edit/delete menu |
| `Drag (on note)` | Move note |
| `Double Click (on note)` | Edit note |

## 🚀 Performance Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + Shift + R` | Clear cache & reload |
| `Ctrl + Shift + P` | Show performance stats |
| `Ctrl + Alt + D` | Toggle debug mode |

## 💡 Tips

### Customization
- Most shortcuts can be customized in settings (Ctrl+,)
- Create custom keyboard macros for repeated tasks
- Use Ctrl+? to see context-sensitive shortcuts

### Efficiency Tips
1. **Sequential Reading**: Use Space for continuous reading
2. **Quick Navigation**: Use Home/End for quick jumps
3. **Search**: Ctrl+F then F3/Shift+F3 for efficient searching
4. **Bookmarks**: Use Ctrl+1-9 for quick page access
5. **Theme Switching**: Ctrl+T for comfortable reading

### Hidden Shortcuts
| Shortcut | Action |
|----------|--------|
| `Ctrl + Shift + Alt + D` | Developer tools |
| `Ctrl + Shift + Alt + C` | Clear all data |
| `Ctrl + Alt + R` | Restart application |

## 🔧 Customization

### Creating Custom Shortcuts

Edit configuration file: `~/.config/lma/shortcuts.json`

```json
{
  "navigation": {
    "next_page": ["Right", "d"],
    "prev_page": ["Left", "a"]
  },
  "annotations": {
    "highlight": ["Ctrl+h", "h"],
    "note": ["Ctrl+n", "n"]
  }
}
```

### Resetting to Defaults

```bash
# Reset all shortcuts to default
rm ~/.config/lma/shortcuts.json
# Restart LMA
```

## 📱 Platform-Specific Notes

### macOS
- Replace `Ctrl` with `Cmd` (⌘)
- `Ctrl + Q` becomes `Cmd + Q`
- Use Mission Control gestures for navigation

### Linux
- All shortcuts work as documented
- Some window managers may conflict with F11
- Consider using `Ctrl + Shift + F` instead

### Windows
- All shortcuts work as documented
- Some antivirus may block certain shortcuts
- Use Windows key shortcuts sparingly

## 🎓 Learning Path

### Beginner (5 shortcuts)
1. `→/←` - Navigate pages
2. `Ctrl + F` - Search
3. `Ctrl + T` - Toggle theme
4. `Space` - Continuous reading
5. `Ctrl + Q` - Quit

### Intermediate (10 additional)
6. `Ctrl + B` - Bookmarks
7. `Ctrl + H` - Highlight
8. `Ctrl + N` - Notes
9. `Ctrl + +/-` - Zoom
10. `Ctrl + G` - Go to page
11. `Ctrl + E` - Export
12. `F3` - Find next
13. `Ctrl + M` - Thumbnails
14. `Home/End` - First/Last page
15. `Ctrl + S` - Save

### Advanced (All shortcuts)
16. Master all annotation shortcuts
17. Learn AI tool shortcuts
18. Customize your own shortcuts
19. Use mouse combinations
20. Create keyboard macros

## 📚 Additional Resources

- [Video Tutorial: Keyboard Shortcuts](https://example.com/tutorial)
- [Customization Guide](docs/customization.md)
- [Accessibility Features](docs/accessibility.md)

## 🐛 Troubleshooting

### Shortcut Not Working?

1. **Check Conflicts**: Some shortcuts may conflict with OS shortcuts
2. **Reset Settings**: Delete `~/.config/lma/shortcuts.json`
3. **Update Application**: Ensure you have the latest version
4. **Check Focus**: Ensure PDF viewer has focus (click on it)

### Reporting Issues

If a shortcut doesn't work:
1. Note the shortcut combination
2. Note your OS and version
3. Open an issue on GitHub with details

---

**Last Updated**: 2024-11-22
**Version**: 1.0.0

*Press `F1` in the application to see this reference anytime!*
