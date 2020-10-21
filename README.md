# RepoKaKaoAlarmBot
카카오톡 봇 채팅 기반 깃허브 관심 레포지토리 등록 서비스 (2020 오픈소스기반기초설계)

## 문서구조(2020.10.21 기준)
.
├── README.md
├── RepoKaKaoAlarm
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── static
    └── admin
        ├── css
        │   ├── autocomplete.css
        │   ├── base.css
        │   ├── changelists.css
        │   ├── dashboard.css
        │   ├── fonts.css
        │   ├── forms.css
        │   ├── login.css
        │   ├── responsive.css
        │   ├── responsive_rtl.css
        │   ├── rtl.css
        │   ├── vendor
        │   │   └── select2
        │   │       ├── LICENSE-SELECT2.md
        │   │       ├── select2.css
        │   │       └── select2.min.css
        │   └── widgets.css
        ├── fonts
        │   ├── LICENSE.txt
        │   ├── README.txt
        │   ├── Roboto-Bold-webfont.woff
        │   ├── Roboto-Light-webfont.woff
        │   └── Roboto-Regular-webfont.woff
        ├── img
        │   ├── LICENSE
        │   ├── README.txt
        │   ├── calendar-icons.svg
        │   ├── gis
        │   │   ├── move_vertex_off.svg
        │   │   └── move_vertex_on.svg
        │   ├── icon-addlink.svg
        │   ├── icon-alert.svg
        │   ├── icon-calendar.svg
        │   ├── icon-changelink.svg
        │   ├── icon-clock.svg
        │   ├── icon-deletelink.svg
        │   ├── icon-no.svg
        │   ├── icon-unknown-alt.svg
        │   ├── icon-unknown.svg
        │   ├── icon-viewlink.svg
        │   ├── icon-yes.svg
        │   ├── inline-delete.svg
        │   ├── search.svg
        │   ├── selector-icons.svg
        │   ├── sorting-icons.svg
        │   ├── tooltag-add.svg
        │   └── tooltag-arrowright.svg
        └── js
            ├── SelectBox.js
            ├── SelectFilter2.js
            ├── actions.js
            ├── actions.min.js
            ├── admin
            │   ├── DateTimeShortcuts.js
            │   └── RelatedObjectLookups.js
            ├── autocomplete.js
            ├── calendar.js
            ├── cancel.js
            ├── change_form.js
            ├── collapse.js
            ├── collapse.min.js
            ├── core.js
            ├── inlines.js
            ├── inlines.min.js
            ├── jquery.init.js
            ├── popup_response.js
            ├── prepopulate.js
            ├── prepopulate.min.js
            ├── prepopulate_init.js
            ├── timeparse.js
            ├── urlify.js
            └── vendor
                ├── jquery
                │   ├── LICENSE.txt
                │   ├── jquery.js
                │   └── jquery.min.js
                ├── select2
                │   ├── LICENSE.md
                │   ├── i18n
                │   │   ├── ar.js
                │   │   ├── az.js
                │   │   ├── bg.js
                │   │   ├── ca.js
                │   │   ├── cs.js
                │   │   ├── da.js
                │   │   ├── de.js
                │   │   ├── el.js
                │   │   ├── en.js
                │   │   ├── es.js
                │   │   ├── et.js
                │   │   ├── eu.js
                │   │   ├── fa.js
                │   │   ├── fi.js
                │   │   ├── fr.js
                │   │   ├── gl.js
                │   │   ├── he.js
                │   │   ├── hi.js
                │   │   ├── hr.js
                │   │   ├── hu.js
                │   │   ├── id.js
                │   │   ├── is.js
                │   │   ├── it.js
                │   │   ├── ja.js
                │   │   ├── km.js
                │   │   ├── ko.js
                │   │   ├── lt.js
                │   │   ├── lv.js
                │   │   ├── mk.js
                │   │   ├── ms.js
                │   │   ├── nb.js
                │   │   ├── nl.js
                │   │   ├── pl.js
                │   │   ├── pt-BR.js
                │   │   ├── pt.js
                │   │   ├── ro.js
                │   │   ├── ru.js
                │   │   ├── sk.js
                │   │   ├── sr-Cyrl.js
                │   │   ├── sr.js
                │   │   ├── sv.js
                │   │   ├── th.js
                │   │   ├── tr.js
                │   │   ├── uk.js
                │   │   ├── vi.js
                │   │   ├── zh-CN.js
                │   │   └── zh-TW.js
                │   ├── select2.full.js
                │   └── select2.full.min.js
                └── xregexp
                    ├── LICENSE.txt
                    ├── xregexp.js
                    └── xregexp.min.js

### Git hub Api 및 DB 관리
최성훈 / 이광열

### Kakao i Open Builder Api 관리 및 Web Front-End 구축
김민주 / 임유빈  

2020. 숭실대학교 오픈소스기반기초설계
