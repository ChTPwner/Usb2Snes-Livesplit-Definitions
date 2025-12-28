# NOTES ON Super Castlevania IV

Shared by SioN on the Castlevania Speedrunning Discord

| Address | Purpose                                                        |
| ------- | -------------------------------------------------------------- |
| 0x0032  | Game State. Equals to 0x04 during Gameplay                     |
| 0x0070  | Related to player control. Equals to 0x05 when player can move |
| 0x0072  | OrbReq. Set to 0x01 when during Orb sequence                   |
| 0x0076  | Orb Timer. Equals to five when player can move                 |
| 0x0086  | Related to Levels                                              |

## Trigger Conditions

### Autostart

0x0070 == 0x05 and 0x0086 == 0x00

### Level Finished

When 0x0086 has the value related to the next level

### Game finished

As the Dracula Orb is grabbed
