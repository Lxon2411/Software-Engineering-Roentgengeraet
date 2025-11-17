## Traceability-Matrix 
| **Requirement-ID**        | **Komponente**                 | **Klasse(n)**                                 | **Schnittstelle(n)**                                                                            |
|---------------------------|--------------------------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------|
| 1.1 (funktional)          | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController``` | ```toggle_radiation()```, ```start_radiation()```, ```stop_radiation()```, ```duration_entry``` |
| 2.1 (funktional)          | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController``` | ```duration_entry.get()```, ```start_radiation()```, ```start()```, ```_run_radiation()```      |
| 3.1 (funktional)          | Steuerungslogik, Systemschicht | ```RadiationController```                     | ```update_progress()```, ```stop()```, ```reset_ui```, ```show_finished_message()```            |
| 1.1<br/>(nichtfunktional) | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController``` | -                                                                                               |
| 1.3<br/>(nichtfunktional) | GUI                            | ```Radiation UI```                            | -                                                                                               |

