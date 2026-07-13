## Developer reference for website creating/updating integration with PetFinder:

https://www.petfinder.com/developers/v2/docs/
https://www.petfinder.com/member/us/ca/lakehead/noahs-ark-animal-haven-rescue-ca2887/


### Petfinder widget HTML for:
https://noahsarkanimalhaven.org/available

# Note: Removed accesstoken value - see bitwarden
```html
<pet-scroller type='[]' age='[]' limit="24"
    status="adoptable"
    petlisttitle="Currently adoptable!"
    organization="CA2887"
    apibase="https://api.petfinder.com"
    petfinderurl="https://www.petfinder.com"
    accesstoken="">
</pet-scroller>
```

```html
<script src="https://www.petfinder.com/assets/widgets/scripts/main-widgets-web.js"></script>
```
