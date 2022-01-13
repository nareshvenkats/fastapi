from typing import Any, Callable, Dict, Optional, Sequence

from fastapi import params
from pydantic.fields import Undefined


def Path(  # noqa: N802
    default: Any,
    *,
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    deprecated: Optional[bool] = None,
    **extra: Any,
) -> Any:
    return params.Path(
        default=default,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        deprecated=deprecated,
        **extra,
    )


def Query(  # noqa: N802
    default: Any,
    *,
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    deprecated: Optional[bool] = None,
    **extra: Any,
) -> Any:
    return params.Query(
        default,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        deprecated=deprecated,
        **extra,
    )


def Header(  # noqa: N802
    default: Any,
    *,
    alias: Optional[str] = None,
    convert_underscores: bool = True,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    deprecated: Optional[bool] = None,
    **extra: Any,
) -> Any:
    return params.Header(
        default,
        alias=alias,
        convert_underscores=convert_underscores,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        deprecated=deprecated,
        **extra,
    )


def Cookie(  # noqa: N802
    default: Any,
    *,
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    deprecated: Optional[bool] = None,
    **extra: Any,
) -> Any:
    return params.Cookie(
        default,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        deprecated=deprecated,
        **extra,
    )


def Body(  # noqa: N802
    default: Any,
    *,
    embed: bool = False,
    media_type: str = "application/json",
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    **extra: Any,
) -> Any:
    return params.Body(
        default,
        embed=embed,
        media_type=media_type,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        **extra,
    )


def Form(  # noqa: N802
    default: Any,
    *,
    media_type: str = "application/x-www-form-urlencoded",
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    **extra: Any,
) -> Any:
    return params.Form(
        default,
        media_type=media_type,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        **extra,
    )


def File(  # noqa: N802
    default: Any,
    *,
    media_type: str = "multipart/form-data",
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    example: Any = Undefined,
    examples: Optional[Dict[str, Any]] = None,
    **extra: Any,
) -> Any:
    return params.File(
        default,
        media_type=media_type,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        example=example,
        examples=examples,
        **extra,
    )


def Depends(  # noqa: N802
    dependency: Optional[Callable[..., Any]] = None, *, use_cache: bool = True
) -> Any:
    return params.Depends(dependency=dependency, use_cache=use_cache)


def Kwargs(spec: Dict[str, Any], *, use_cache: bool = True) -> Any:  # noqa: N802
    return params.Kwargs(spec=spec, use_cache=use_cache)


def Security(  # noqa: N802
    dependency: Optional[Callable[..., Any]] = None,
    *,
    scopes: Optional[Sequence[str]] = None,
    use_cache: bool = True,
) -> Any:
    return params.Security(dependency=dependency, scopes=scopes, use_cache=use_cache)
