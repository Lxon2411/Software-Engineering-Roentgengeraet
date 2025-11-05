## Traceability-Matrix 
| **Requirement-ID**        | **Komponente**                 | **Klasse(n)**                                                  | **Schnittstelle(n)**                                                                      |
|---------------------------|--------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 1.1 (funktional)          | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController```                  | ```toggle_radiation()```, ```start_radiation()```, ```stop_radiation()```                 |
| 2.1 (funktional)          | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController```                  | ```duration_entry.get()```, ```start_radiation()```                                       |
| 3.1 (funktional)          | Steuerungslogik, Systemschicht | ```RadiationController```                                      | ```update_timer()```, ```time.time()```, ```winsound.Beep()```                            |
| 4.1 (funktional)          | GUI, Steuerungslogik           | ```StatusLED```, ```Radiation UI```, ```RadiationController``` | ```set_on()```, ```set_off()```, ```progress['value']```, ```timer_label.config()```      |
| 5.1 (funktional)          | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController```                  | ```log_message()```, ```log_text.insert()```                                              |
| 5.2 (funktional)          | GUI, Steuerungslogik           | ```RadiationController```                                      | ```messagebox.showerror()```, ```messagebox.showinfo()```, ```messagebox.showwarning()``` |
| 1.1<br/>(nichtfunktional) | GUI                            |                                                                |                                                                                           |
| 1.2<br/>(nichtfunktional) | GUI                            |                                                                |                                                                                           |
| 1.3<br/>(nichtfunktional) | GUI                            |                                                                |                                                                                           |
| 1.4<br/>(nichtfunktional) | GUI                            |                                                                |                                                                                           |
| 1.5<br/>(nichtfunktional) | GUI                            |                                                                |                                                                                           |

