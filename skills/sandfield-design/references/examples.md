# Examples: good vs. not yet

Short contrasts for the places generated UIs most often go wrong. The domains are deliberately mixed. Use the brief's domain, never the one in these examples.

## Empty states

| Not yet | Good |
|---|---|
| "No data" | "No invoices yet. Invoices appear here once an order is approved. `[ Create invoice ]`" |
| "No results" (after filtering) | "No tickets match *Status: Waiting* and *Team: Billing*. `[ Clear filters ]`" |

## Errors

| Not yet | Good |
|---|---|
| "Something went wrong." | "Couldn't load timesheets: the payroll service didn't respond. Your other data is unaffected. `[ Try again ]`" |
| "Invalid input" | "Enter a quantity in units, e.g. 250" (next to the field, value kept) |

## Buttons

| Not yet | Good |
|---|---|
| `[ OK ]` on a delete dialog | `[ Delete 3 contacts ]` |
| `[ Continue ]` on the last wizard step | `[ Submit application ]` |
| `[ Submit ]` `[ Save ]` `[ Send ]` all primary | One primary `[ Send to approver ]`; `Save draft` secondary |

## Wizard footer

```
Not yet:  [ Cancel ] [ Back ] [ Next ]            (order varies, scrolls away)

Good:     [ Back ]                    [ Cancel ]  [ Continue ]
          ─────────── sticky to the bottom of the viewport ───────────
```

## Tables

```
Not yet:  every row has Edit / Delete / Archive buttons; bulk bar always visible

Good:     row actions in an overflow (⋯); select rows →
          "3 selected  [ Archive ]  [ Delete ]  Clear selection"
          numbers right-aligned with units: 1,250.00 kg
```

## Destructive action

```
Not yet:  "Are you sure?"  [ Yes ] [ No ]

Good:     "Delete the Northside team?
           This removes 14 members' access and cannot be undone."
          [ Cancel ]  [ Delete team ]      ← Cancel has default focus
```
