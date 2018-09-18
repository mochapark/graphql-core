"""GraphQL-core-next

The primary `graphql` package includes everything you need to define a GraphQL
schema and fulfill GraphQL requests.

GraphQL-core-next provides a reference implementation for the GraphQL
specification but is also a useful utility for operating on GraphQL files
and building sophisticated tools.

This top-level package exports a general purpose function for fulfilling all
steps of the GraphQL specification in a single operation, but also includes
utilities for every part of the GraphQL specification:

  - Parsing the GraphQL language.
  - Building a GraphQL type schema.
  - Validating a GraphQL request against a type schema.
  - Executing a GraphQL request against a type schema.

This also includes utility functions for operating on GraphQL types and
GraphQL documents to facilitate building tools.

You may also import from each sub-package directly. For example, the
following two import statements are equivalent::

    from graphql import parse
    from graphql.language import parse

The sub-packages of GraphQL-core-next are:

  - `graphql/language`: Parse and operate on the GraphQL language.
  - `graphql/type`: Define GraphQL types and schema.
  - `graphql/validation`: The Validation phase of fulfilling a GraphQL result.
  - `graphql/execution`: The Execution phase of fulfilling a GraphQL request.
  - `graphql/error`: Creating and format GraphQL errors.
  - `graphql/utilities`:
     Common useful computations upon the GraphQL language and type objects.
  - `graphql/subscription`: Subscribe to data updates.
"""

__version__ = "1.0.1"
__version_js__ = "14.0.2"

# The primary entry point into fulfilling a GraphQL request.

from .graphql import graphql, graphql_sync

# Create and operate on GraphQL type definitions and schema.
from .type import (
    GraphQLSchema,
    # Definitions
    GraphQLScalarType,
    GraphQLObjectType,
    GraphQLInterfaceType,
    GraphQLUnionType,
    GraphQLEnumType,
    GraphQLInputObjectType,
    GraphQLList,
    GraphQLNonNull,
    GraphQLDirective,
    # "Enum" of Type Kinds
    TypeKind,
    # Scalars
    specified_scalar_types,
    GraphQLInt,
    GraphQLFloat,
    GraphQLString,
    GraphQLBoolean,
    GraphQLID,
    # Built-in Directives defined by the Spec
    specified_directives,
    GraphQLIncludeDirective,
    GraphQLSkipDirective,
    GraphQLDeprecatedDirective,
    # Constant Deprecation Reason
    DEFAULT_DEPRECATION_REASON,
    # Meta-field definitions.
    SchemaMetaFieldDef,
    TypeMetaFieldDef,
    TypeNameMetaFieldDef,
    # GraphQL Types for introspection.
    introspection_types,
    # Predicates
    is_schema,
    is_directive,
    is_type,
    is_scalar_type,
    is_object_type,
    is_interface_type,
    is_union_type,
    is_enum_type,
    is_input_object_type,
    is_list_type,
    is_non_null_type,
    is_input_type,
    is_output_type,
    is_leaf_type,
    is_composite_type,
    is_abstract_type,
    is_wrapping_type,
    is_nullable_type,
    is_named_type,
    is_required_argument,
    is_required_input_field,
    is_specified_scalar_type,
    is_introspection_type,
    is_specified_directive,
    # Assertions
    assert_type,
    assert_scalar_type,
    assert_object_type,
    assert_interface_type,
    assert_union_type,
    assert_enum_type,
    assert_input_object_type,
    assert_list_type,
    assert_non_null_type,
    assert_input_type,
    assert_output_type,
    assert_leaf_type,
    assert_composite_type,
    assert_abstract_type,
    assert_wrapping_type,
    assert_nullable_type,
    assert_named_type,
    # Un-modifiers
    get_nullable_type,
    get_named_type,
    # Validate GraphQL schema.
    validate_schema,
    assert_valid_schema,
    # Types
    GraphQLType,
    GraphQLInputType,
    GraphQLOutputType,
    GraphQLLeafType,
    GraphQLCompositeType,
    GraphQLAbstractType,
    GraphQLWrappingType,
    GraphQLNullableType,
    GraphQLNamedType,
    Thunk,
    GraphQLArgument,
    GraphQLArgumentMap,
    GraphQLEnumValue,
    GraphQLEnumValueMap,
    GraphQLField,
    GraphQLFieldMap,
    GraphQLFieldResolver,
    GraphQLInputField,
    GraphQLInputFieldMap,
    GraphQLScalarSerializer,
    GraphQLScalarValueParser,
    GraphQLScalarLiteralParser,
    GraphQLIsTypeOfFn,
    GraphQLResolveInfo,
    ResponsePath,
    GraphQLTypeResolver,
)

# Parse and operate on GraphQL language source files.
from .language import (
    Source,
    get_location,
    # Parse
    parse,
    parse_value,
    parse_type,
    # Print
    print_ast,
    # Visit
    visit,
    ParallelVisitor,
    TypeInfoVisitor,
    Visitor,
    TokenKind,
    DirectiveLocation,
    BREAK,
    SKIP,
    REMOVE,
    IDLE,
    # Predicates
    is_definition_node,
    is_executable_definition_node,
    is_selection_node,
    is_value_node,
    is_type_node,
    is_type_system_definition_node,
    is_type_definition_node,
    is_type_system_extension_node,
    is_type_extension_node,
    # Types
    Lexer,
    SourceLocation,
    # AST nodes
    Location,
    Token,
    NameNode,
    DocumentNode,
    DefinitionNode,
    ExecutableDefinitionNode,
    OperationDefinitionNode,
    OperationType,
    VariableDefinitionNode,
    VariableNode,
    SelectionSetNode,
    SelectionNode,
    FieldNode,
    ArgumentNode,
    FragmentSpreadNode,
    InlineFragmentNode,
    FragmentDefinitionNode,
    ValueNode,
    IntValueNode,
    FloatValueNode,
    StringValueNode,
    BooleanValueNode,
    NullValueNode,
    EnumValueNode,
    ListValueNode,
    ObjectValueNode,
    ObjectFieldNode,
    DirectiveNode,
    TypeNode,
    NamedTypeNode,
    ListTypeNode,
    NonNullTypeNode,
    TypeSystemDefinitionNode,
    SchemaDefinitionNode,
    OperationTypeDefinitionNode,
    TypeDefinitionNode,
    ScalarTypeDefinitionNode,
    ObjectTypeDefinitionNode,
    FieldDefinitionNode,
    InputValueDefinitionNode,
    InterfaceTypeDefinitionNode,
    UnionTypeDefinitionNode,
    EnumTypeDefinitionNode,
    EnumValueDefinitionNode,
    InputObjectTypeDefinitionNode,
    DirectiveDefinitionNode,
    TypeSystemExtensionNode,
    SchemaExtensionNode,
    TypeExtensionNode,
    ScalarTypeExtensionNode,
    ObjectTypeExtensionNode,
    InterfaceTypeExtensionNode,
    UnionTypeExtensionNode,
    EnumTypeExtensionNode,
    InputObjectTypeExtensionNode,
)

# Execute GraphQL queries.
from .execution import (
    execute,
    default_field_resolver,
    response_path_as_list,
    get_directive_values,
    # Types
    ExecutionContext,
    ExecutionResult,
)

from .subscription import subscribe, create_source_event_stream


# Validate GraphQL queries.
from .validation import (
    validate,
    ValidationContext,
    ValidationRule,
    ASTValidationRule,
    SDLValidationRule,
    # All validation rules in the GraphQL Specification.
    specified_rules,
    # Individual validation rules.
    FieldsOnCorrectTypeRule,
    FragmentsOnCompositeTypesRule,
    KnownArgumentNamesRule,
    KnownDirectivesRule,
    KnownFragmentNamesRule,
    KnownTypeNamesRule,
    LoneAnonymousOperationRule,
    NoFragmentCyclesRule,
    NoUndefinedVariablesRule,
    NoUnusedFragmentsRule,
    NoUnusedVariablesRule,
    OverlappingFieldsCanBeMergedRule,
    PossibleFragmentSpreadsRule,
    ProvidedRequiredArgumentsRule,
    ScalarLeafsRule,
    SingleFieldSubscriptionsRule,
    UniqueArgumentNamesRule,
    UniqueDirectivesPerLocationRule,
    UniqueFragmentNamesRule,
    UniqueInputFieldNamesRule,
    UniqueOperationNamesRule,
    UniqueVariableNamesRule,
    ValuesOfCorrectTypeRule,
    VariablesAreInputTypesRule,
    VariablesInAllowedPositionRule,
)

# Create, format, and print GraphQL errors.
from .error import GraphQLError, format_error, print_error

# Utilities for operating on GraphQL type schema and parsed sources.
from .utilities import (
    # Produce the GraphQL query recommended for a full schema introspection.
    # Accepts optional IntrospectionOptions.
    get_introspection_query,
    # Gets the target Operation from a Document
    get_operation_ast,
    # Gets the Type for the target Operation AST.
    get_operation_root_type,
    # Convert a GraphQLSchema to an IntrospectionQuery
    introspection_from_schema,
    # Build a GraphQLSchema from an introspection result.
    build_client_schema,
    # Build a GraphQLSchema from a parsed GraphQL Schema language AST.
    build_ast_schema,
    # Build a GraphQLSchema from a GraphQL schema language document.
    build_schema,
    # @deprecated: Get the description from a schema AST node.
    get_description,
    # Extends an existing GraphQLSchema from a parsed GraphQL Schema
    # language AST.
    extend_schema,
    # Sort a GraphQLSchema.
    lexicographic_sort_schema,
    # Print a GraphQLSchema to GraphQL Schema language.
    print_schema,
    # Prints the built-in introspection schema in the Schema Language
    # format.
    print_introspection_schema,
    # Print a GraphQLType to GraphQL Schema language.
    print_type,
    # Create a GraphQLType from a GraphQL language AST.
    type_from_ast,
    # Create a Python value from a GraphQL language AST with a Type.
    value_from_ast,
    # Create a Python value from a GraphQL language AST without a Type.
    value_from_ast_untyped,
    # Create a GraphQL language AST from a Python value.
    ast_from_value,
    # A helper to use within recursive-descent visitors which need to be aware
    # of the GraphQL type system.
    TypeInfo,
    # Coerces a Python value to a GraphQL type, or produces errors.
    coerce_value,
    # Concatenates multiple AST together.
    concat_ast,
    # Separates an AST into an AST per Operation.
    separate_operations,
    # Comparators for types
    is_equal_type,
    is_type_sub_type_of,
    do_types_overlap,
    # Asserts a string is a valid GraphQL name.
    assert_valid_name,
    # Determine if a string is a valid GraphQL name.
    is_valid_name_error,
    # Compares two GraphQLSchemas and detects breaking changes.
    find_breaking_changes,
    find_dangerous_changes,
    BreakingChange,
    BreakingChangeType,
    DangerousChange,
    DangerousChangeType,
)

__all__ = [
    "graphql",
    "graphql_sync",
    "GraphQLSchema",
    "GraphQLScalarType",
    "GraphQLObjectType",
    "GraphQLInterfaceType",
    "GraphQLUnionType",
    "GraphQLEnumType",
    "GraphQLInputObjectType",
    "GraphQLList",
    "GraphQLNonNull",
    "GraphQLDirective",
    "TypeKind",
    "specified_scalar_types",
    "GraphQLInt",
    "GraphQLFloat",
    "GraphQLString",
    "GraphQLBoolean",
    "GraphQLID",
    "specified_directives",
    "GraphQLIncludeDirective",
    "GraphQLSkipDirective",
    "GraphQLDeprecatedDirective",
    "DEFAULT_DEPRECATION_REASON",
    "SchemaMetaFieldDef",
    "TypeMetaFieldDef",
    "TypeNameMetaFieldDef",
    "introspection_types",
    "is_schema",
    "is_directive",
    "is_type",
    "is_scalar_type",
    "is_object_type",
    "is_interface_type",
    "is_union_type",
    "is_enum_type",
    "is_input_object_type",
    "is_list_type",
    "is_non_null_type",
    "is_input_type",
    "is_output_type",
    "is_leaf_type",
    "is_composite_type",
    "is_abstract_type",
    "is_wrapping_type",
    "is_nullable_type",
    "is_named_type",
    "is_required_argument",
    "is_required_input_field",
    "is_specified_scalar_type",
    "is_introspection_type",
    "is_specified_directive",
    "assert_type",
    "assert_scalar_type",
    "assert_object_type",
    "assert_interface_type",
    "assert_union_type",
    "assert_enum_type",
    "assert_input_object_type",
    "assert_list_type",
    "assert_non_null_type",
    "assert_input_type",
    "assert_output_type",
    "assert_leaf_type",
    "assert_composite_type",
    "assert_abstract_type",
    "assert_wrapping_type",
    "assert_nullable_type",
    "assert_named_type",
    "get_nullable_type",
    "get_named_type",
    "validate_schema",
    "assert_valid_schema",
    "GraphQLType",
    "GraphQLInputType",
    "GraphQLOutputType",
    "GraphQLLeafType",
    "GraphQLCompositeType",
    "GraphQLAbstractType",
    "GraphQLWrappingType",
    "GraphQLNullableType",
    "GraphQLNamedType",
    "Thunk",
    "GraphQLArgument",
    "GraphQLArgumentMap",
    "GraphQLEnumValue",
    "GraphQLEnumValueMap",
    "GraphQLField",
    "GraphQLFieldMap",
    "GraphQLFieldResolver",
    "GraphQLInputField",
    "GraphQLInputFieldMap",
    "GraphQLScalarSerializer",
    "GraphQLScalarValueParser",
    "GraphQLScalarLiteralParser",
    "GraphQLIsTypeOfFn",
    "GraphQLResolveInfo",
    "ResponsePath",
    "GraphQLTypeResolver",
    "Source",
    "get_location",
    "parse",
    "parse_value",
    "parse_type",
    "print_ast",
    "visit",
    "ParallelVisitor",
    "TypeInfoVisitor",
    "Visitor",
    "TokenKind",
    "DirectiveLocation",
    "BREAK",
    "SKIP",
    "REMOVE",
    "IDLE",
    "is_definition_node",
    "is_executable_definition_node",
    "is_selection_node",
    "is_value_node",
    "is_type_node",
    "is_type_system_definition_node",
    "is_type_definition_node",
    "is_type_system_extension_node",
    "is_type_extension_node",
    "Lexer",
    "SourceLocation",
    "Location",
    "Token",
    "NameNode",
    "DocumentNode",
    "DefinitionNode",
    "ExecutableDefinitionNode",
    "OperationDefinitionNode",
    "OperationType",
    "VariableDefinitionNode",
    "VariableNode",
    "SelectionSetNode",
    "SelectionNode",
    "FieldNode",
    "ArgumentNode",
    "FragmentSpreadNode",
    "InlineFragmentNode",
    "FragmentDefinitionNode",
    "ValueNode",
    "IntValueNode",
    "FloatValueNode",
    "StringValueNode",
    "BooleanValueNode",
    "NullValueNode",
    "EnumValueNode",
    "ListValueNode",
    "ObjectValueNode",
    "ObjectFieldNode",
    "DirectiveNode",
    "TypeNode",
    "NamedTypeNode",
    "ListTypeNode",
    "NonNullTypeNode",
    "TypeSystemDefinitionNode",
    "SchemaDefinitionNode",
    "OperationTypeDefinitionNode",
    "TypeDefinitionNode",
    "ScalarTypeDefinitionNode",
    "ObjectTypeDefinitionNode",
    "FieldDefinitionNode",
    "InputValueDefinitionNode",
    "InterfaceTypeDefinitionNode",
    "UnionTypeDefinitionNode",
    "EnumTypeDefinitionNode",
    "EnumValueDefinitionNode",
    "InputObjectTypeDefinitionNode",
    "DirectiveDefinitionNode",
    "TypeSystemExtensionNode",
    "SchemaExtensionNode",
    "TypeExtensionNode",
    "ScalarTypeExtensionNode",
    "ObjectTypeExtensionNode",
    "InterfaceTypeExtensionNode",
    "UnionTypeExtensionNode",
    "EnumTypeExtensionNode",
    "InputObjectTypeExtensionNode",
    "execute",
    "default_field_resolver",
    "response_path_as_list",
    "get_directive_values",
    "ExecutionContext",
    "ExecutionResult",
    "subscribe",
    "create_source_event_stream",
    "validate",
    "ValidationContext",
    "ValidationRule",
    "ASTValidationRule",
    "SDLValidationRule",
    "specified_rules",
    "FieldsOnCorrectTypeRule",
    "FragmentsOnCompositeTypesRule",
    "KnownArgumentNamesRule",
    "KnownDirectivesRule",
    "KnownFragmentNamesRule",
    "KnownTypeNamesRule",
    "LoneAnonymousOperationRule",
    "NoFragmentCyclesRule",
    "NoUndefinedVariablesRule",
    "NoUnusedFragmentsRule",
    "NoUnusedVariablesRule",
    "OverlappingFieldsCanBeMergedRule",
    "PossibleFragmentSpreadsRule",
    "ProvidedRequiredArgumentsRule",
    "ScalarLeafsRule",
    "SingleFieldSubscriptionsRule",
    "UniqueArgumentNamesRule",
    "UniqueDirectivesPerLocationRule",
    "UniqueFragmentNamesRule",
    "UniqueInputFieldNamesRule",
    "UniqueOperationNamesRule",
    "UniqueVariableNamesRule",
    "ValuesOfCorrectTypeRule",
    "VariablesAreInputTypesRule",
    "VariablesInAllowedPositionRule",
    "GraphQLError",
    "format_error",
    "print_error",
    "get_introspection_query",
    "get_operation_ast",
    "get_operation_root_type",
    "introspection_from_schema",
    "build_client_schema",
    "build_ast_schema",
    "build_schema",
    "get_description",
    "extend_schema",
    "lexicographic_sort_schema",
    "print_schema",
    "print_introspection_schema",
    "print_type",
    "type_from_ast",
    "value_from_ast",
    "value_from_ast_untyped",
    "ast_from_value",
    "TypeInfo",
    "coerce_value",
    "concat_ast",
    "separate_operations",
    "is_equal_type",
    "is_type_sub_type_of",
    "do_types_overlap",
    "assert_valid_name",
    "is_valid_name_error",
    "find_breaking_changes",
    "find_dangerous_changes",
    "BreakingChange",
    "BreakingChangeType",
    "DangerousChange",
    "DangerousChangeType",
]
